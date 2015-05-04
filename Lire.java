

//lire

import java.io.*;

import java.util.ArrayList;











/**
 
 
 
 * @author moh
 
 
 
 *
 
 
 
 */



public class Lire {
    
    
    
    
    
    
    
    /**
     
     
     
     * DÃ©monstration simplissible de lecture ligne par ligne sur l'entrÃ©e standard.
     
     
     
     */
    
    
    
    public static ArrayList<ArrayList<String>> Lecture() {
        
        
        
        
        
        //Liste de liste pour transformer mon fichier en matrice
        
        
        
        ArrayList<ArrayList<String>> k=new ArrayList<ArrayList<String>>();
        
        
        
        
        
        // On ouvre l'entrÃ©e standard
        
        
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        
        
        // uneLigne va stocker la ligne lue
        
        
        
        
        
        String uneLigne = null;
        
        
        
        // CONTINUER indique s'il y a encore des choses Ã  lire ou si on a terminÃ©.
        
        
        
        boolean continuer = true;
        
        
        
        int i=0;
        
        
        
        while ( continuer ) {
            
            
            
            try {
                
                
                
                
                
                uneLigne = br.readLine();
                
                
                
                
                
                
                
                
                
                if ( uneLigne != null && ! uneLigne.startsWith("#")) {
                    
                    
                    
                    //System.out.println( k.get(0) );
                    
                    
                    
                    // on supprime les espaces multiples
                    
                    ArrayList<String> l=new ArrayList<String>();
                    
                    
                    
                    
                    
                    uneLigne.replaceAll( "\\s+", " " );
                    
                    
                    
                    
                    
                    for ( String s : uneLigne.split( " " ) ) {
                        
                        
                        
                        
                        
                        
                        
                        if ( s.length() > 0 ) {
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            l.add(s);
                            
                            
                            
                            
                            
                        }
                        
                        
                        
                    }
                    
                    
                    
                    k.add(i,l);
                    
                    
                    
                    i=i+1;
                    
                    
                    
                    System.out.println( "" );
                    
                    
                    
                }
                
                // on regarde si une ligne est un commentaire alors on la saute
                
                
                
                else if(uneLigne != null && uneLigne.startsWith("#")){
                    
                    continuer=true;}
                
                else {
                    
                    
                    
                    continuer = false;
                    
                    
                    
                }
                
                
                
                
                
                
                
            } catch (IOException ioe) {
                
                
                
                System.out.println( "Erreur de lecture" );
                
                
                
                System.exit(1);
                
            }
            
        }
        
        affiche2(k);
        
        
        
        return k;
        
        
        
    }
    
    
    
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    public static void affiche2(ArrayList<ArrayList<String>> m){
        
        
        
        for(int i =0 ; i < m.size();i++){
            
            System.out.println("");
            
            
            
            for(int j =0 ; j < m.get(i).size();j++){
                
                
                
                System.out.print(m.get(i).get(j) + " ");}
            
        }
        
        System.out.println();
        
        
        
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}