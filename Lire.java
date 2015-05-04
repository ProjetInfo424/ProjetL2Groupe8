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
        
        affiche1(k);
        
        
        
        return k;
        
        
        
    }
    

    
    
    
    // recreer la matrice avec un tableau de tableau de tableau pour ranger par (r,g,b)
    
    
    public  static  ArrayList<ArrayList<ArrayList<String>>> matriceppm(){
        
        ArrayList<ArrayList<String>> ma= Lire.Lecture();
      
        ArrayList<ArrayList<ArrayList<String>>> tab1 =new  ArrayList<ArrayList<ArrayList<String>>>();
        int i=3;
        int j=0;
        System.out.println( ma.get(i).size() );

        
        
        while (i  +2< ma.size() -1) {

            ArrayList<ArrayList<String>> tab2 = new ArrayList<ArrayList<String>>();


            
            while(j<ma.get(i).size() ){
                

                ArrayList<String> tab3= new ArrayList<String>(3) ;

               
                tab3.add(ma.get(i).get(j));
                tab3.add(ma.get(i).get(j+1));
                tab3.add(ma.get(i).get(j+2));
                
                tab2.add(tab3);
                j=j+3;

            }
            tab1.add(tab2);

            i=i+1;
        }
        System.out.println(  ma.get(7).get(2));
        

        affiche2(tab1);
        
        return tab1;
    }
        
    
    
    
    
  // afficher un tableau 2D
    
    public static void affiche1(ArrayList<ArrayList<String>> m){
        
        
        
        for(int i =0 ; i < m.size();i++){
            
            System.out.println("");
            
            
            
            for(int j =0 ; j < m.get(i).size();j++){
                
                
                
                System.out.print(m.get(i).get(j) + " ");}
            
        }
        
        System.out.println();
        
        
        
    }
    
   //afficher un tableau 2D d'element de tableau im
    
    
    public static void affiche2( ArrayList<ArrayList<ArrayList<String>>> m){
        
        
        
        for(int i =0 ; i < m.size();i++){
            
            System.out.println("");
            
            
            
            for(int j =0 ; j < m.get(i).size();j++){
                
                
                
                System.out.print(m.get(i).get(j) + " ");
            }
            
        }
        
        System.out.println();
        
        
        
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}