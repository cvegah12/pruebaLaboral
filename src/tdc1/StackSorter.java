/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tdc1;

import java.util.Stack;

/**
 *
 * @author Camilo Vega
 */
public class StackSorter {
    
    
    public Stack<Integer> Sort(Stack<Integer> stackA){
        Stack<Integer> stackB = new Stack<Integer>();
        Integer t = 0;
        while(!stackA.empty()){
            
            
            
            // se dejan numeros en B hasta que haya uno mayor al actual en B
            //Ese procede a dejarse en la variable auxiliar T.
            
            do{
                printResults((Stack<Integer>)stackA.clone(),(Stack<Integer>)stackB.clone(),t);
                stackB.push(stackA.pop());
            }while(stackA.empty() ? false : stackA.peek()<stackB.peek());
            if(!stackA.empty()){
                printResults((Stack<Integer>)stackA.clone(),(Stack<Integer>)stackB.clone(),t);
                t = stackA.pop();
            }
            
            // Se devuelve al stack A hasta tener un número mayor que el almacenado en t
            
            while (stackB.empty() || stackA.empty() ? false : stackB.peek()<t){

                printResults((Stack<Integer>)stackA.clone(),(Stack<Integer>)stackB.clone(),t);
                stackA.push(stackB.pop());
            }
            printResults((Stack<Integer>)stackA.clone(),(Stack<Integer>)stackB.clone(),t);
            stackB.push(t);
        }
        return stackB;
    }
    
    
    private void printResults(Stack A, Stack B, Integer t){
        System.out.print("\nStack A = ");
        if(A.empty())
            System.out.print("vacío ");
        while(!A.empty())
            System.out.print(A.pop()+" ");
        System.out.print("\nStack B = ");
        if(B.empty())
            System.out.print("vacío ");
        while(!B.empty()){
            System.out.print(B.pop()+" ");
        }
        System.out.print("\nt= "+t);
    }
}
