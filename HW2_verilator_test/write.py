front = '''
#include <verilated.h>          // Defines common routines
//# include <iostream>             // Need std::cout
#include <Vour.h>               // From Verilating "top.v"

Vour *top;                      // Instantiation of module

vluint64_t main_time = 0;       // Current simulation time
        // This is a 64-bit integer to reduce wrap over issues and
        // allow modulus.  You can also use a double, if you wish.

double sc_time_stamp () {       // Called by $time in Verilog
    return main_time;           // converts to double, to match
                                // what SystemC does
}

int main(int argc, char** argv) {
    Verilated::commandArgs(argc, argv);   // Remember args

    top = new Vour;             // Create instance

    // top->reset_l = 0;           // Set some inputs

    while (!Verilated::gotFinish()) {'''
def back(toT):
    back = '''
            top->eval();            // Evaluate model
            printf("%d\\n",top->MuxOut);       // Read a output
            main_time++;            // Time passes...
            if (main_time == '''+str(toT)+'''){
                int main_time_int = main_time; //because the type of main_time is not acceptable in printf()
                printf("time = %d\\n", main_time_int);
                break;
            }
        }
        top->final();               // Done simulating
        //    // (Though this example doesn't get here)
         delete top;
    }\n
    '''
    return back
def evaluate(each):
    posi, a = each.split('\'b')
    # a = equ[1]
    x = int(a,2)
    posi = posi.split('=')[0]
    return [posi, x]
def assign(s):
    final = ''
    for each in s:
        final += '    '*(n+1) + each + '\n'
    return final
import sys
tb_name = sys.argv[1]
n = 2
fin = open(tb_name,'r')
fout = open('sim_main.cpp','w')
fout.write(front+'\n')
fromT = 0
toT = 0
for line in fin:
    if '#' not in line: continue
    element = line.split("#")
    if '//' in element[0]: continue
    time = int(element[1].split(' ')[0])
    # print(element[1])
    statement = element[1].split(' ')[1].split(';')[:-1]
    eqlist = []
    for each in statement:
        if '\'b' in each: eq = evaluate(each)
        else: eq = each.split('=')
        # print(eq)
        writed = 'top->%s=%s;'%(eq[0],eq[1])
        eqlist.append(writed)
    fromT = toT
    toT += time
    fout.write('    '*n+f'if (main_time >= {fromT} && main_time < {toT}) {{\n{assign(eqlist)}}}\n')
        # T = tuple(element[1].rstrip(' '))[1:]

        # inputt.append(T)
    # return inputt[1:], len(inputt)-1
back = back(toT)
fout.write(back)
# f=open('sim_main.cpp','w')
# f.write('* %s: %s responses' %(fileName[:-6], length))
fin.close()
fout.close()

