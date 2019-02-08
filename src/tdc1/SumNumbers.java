/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tdc1;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

/**
 *
 * @author Camilo Vega
 */
public class SumNumbers {
    
    public int sumNumbers(String s){
        int sum = 0;
        Pattern p = Pattern.compile("\\d+");
        Matcher m = p.matcher(s);
        while (m.find()){
            sum+= Integer.parseInt(m.group());
        }
        
        return sum;
        /*int ind1,ind2;
        ind1=s.indexOf("(\\d+)");
        ind2=s.lastIndexOf("(\\d+)");
        System.out.println(ind1+ " " +ind2);
        System.out.print(s.substring(ind1, ind2));*/
    }
    
    public int sumNumbersAlt(String s) {
        int sum = 0;
        boolean chain = false;
        String aux = "";
        //empezar a recorrer el string
        for (int i = 0; i<s.length();i++){
            if(s.charAt(i) > 47 && s.charAt(i)<58){
                if(!chain){
                    chain=true;
                    aux = "";
                }
                aux += s.charAt(i);
            }
            else{
                if(chain){
                    chain= false;
                    sum += Integer.parseInt(aux);
                }
            }   
        }
        sum += Integer.parseInt(aux);
        
        return sum;
    }
}
