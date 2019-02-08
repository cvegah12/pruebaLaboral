/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tdc1;

import java.util.Random;
import java.util.Stack;

/**
 *
 * @author Camilo Vega
 */
public class TDC1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        // Descomentar ejercicio que se quiera ver.
        
        // ej1() 
        // ej2()
        // ej3()
        

    }
    
    static void ej1(){
        Stack<Integer> stackA = new Stack<Integer>();
        stackA.push(2);
        stackA.push(0);
        stackA.push(3);
        stackA.push(9);
        stackA.push(7);
        stackA.push(5);
        stackA.push(6);
        stackA.push(1);
        stackA.push(8);
        stackA.push(4);
        StackSorter sorter = new StackSorter();
        stackA = sorter.Sort(stackA);
        while(!stackA.empty()){
            System.out.print(stackA.pop()+"\n");
        }
    }
    static void ej2(){
        SumNumbers sn = new SumNumbers();
        System.out.println(sn.sumNumbers("aa11b33"));
        System.out.println(sn.sumNumbersAlt("aa11b33"));
    }
    
    static void ej3(){
        Kdom kd = new Kdom();
        System.out.println(kd.kDomSearch("sdfshkssrfatweqsrqsswra"));
    }
}
