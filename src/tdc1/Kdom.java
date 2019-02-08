/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tdc1;

/**
 *
 * @author Camilo Vega
 */
public class Kdom {
    
    
    public int kDomSearch(String S){
        
        String sub = ""; // almacenará los substrings a analizar.
        int counter = 0; // cuenta las repeticiones de 
        
        for (int k=0; k<S.length();k++){ //recorre los k para encontrar un k-dominante
            
            for(char c=97; c<123; c++){ //recorre cada caracter
                counter = 0;
                for (int i= 0; i<S.length()-k;i++){ //recorre cada substring
                    sub = S.substring(i,i+k+1);
                    if(sub.contains(String.valueOf(c))){
                        counter++;
                    }else{
                        i = S.length();
                    }
                }
                if(counter == S.length()-k)
                    return k+1;
                
            }
            
            
            
        }
            
        
        
        
        return S.length();
    }
    
    
}
