
//ANALYSÉ

import java.util.ArrayList;







public class Figure {
    
    private static String cc;
    
    private static String cp;
    
    
    
    public Figure() {
        
        cp=null;
        
        cc=null;
        
        
        
        
        
    }
    
    
    
    public static void descriptionimage(){
        
        testforme(analyseform());
        
    }
    
    
    
    
    
    
    
    public  static ArrayList<Integer>  analyseform() {
        
        ArrayList<ArrayList<String>> k= Lire.Lecture();
        
        ArrayList<Integer> l=new ArrayList<Integer>();
        
        int z=0;
        
        boolean estrectangle=false;
        
        String v=null;
        
        int a=0;
        
        int b=0;
        
        
        
        
        
        for  (int i=3 ;i  < k.size() ; i++) {
            
            
            
            int compteur=0;
            
            
            
            for (int j=0; j + 1 < k.get(i).size() -1; j++){
                
                
                
                setCp(k.get(i).get(j));
                
                setCc(k.get(i).get(j+1));
                
                
                
                if (! (getCc().equals(getCp()) )){
                    
                    System.out.println();
                    
                    
                    
                    a = k.indexOf(k.get(i));
                    
                    
                    
                    System.out.println();
                    
                    
                    
                    
                    
                    
                    b= k.indexOf(k.get(j));
                    
                    
                    
                    
                    
                    
                    System.out.println();
                    
                    
                    
                    if( (k.get(i).get(j)).equals(k.get(8).get(3))){
                        
                        
                        
                        compteur=compteur+1;
                        
                    }
                    
                    
                    
                    
                    
                    if ( (k.get(i)).equals(k.get(i + 1)) ){
                        
                        estrectangle=true;
                        
                    }
                    
                }
                
            }
            
            l.add(compteur);
            
        }
        
        
        
        
        
        
        
        if (estrectangle){
            
            System.out.print("Forme de l'image : Rectangle");
            
        }
        
        
        
        System.out.println();
        
        if (k.get(0).get(0).equals("P2")){
            
            System.out.print("Format de l'image: PGM");}
        
        else if (k.get(0).get(0).equals("P3")){
            
            System.out.print("Format de l'image: PPM");}
        
        System.out.println();
        
        System.out.print( "Dimension de l'image (LARGEUR,HAUTEUR): " + "(" + k.get(1).get(0) + "," + k.get(1).get(1) + ")" );
        
        System.out.println();
        
        System.out.print("Couleur maximal de l'image: " + k.get(2).get(0));
        
        System.out.println();
        
        return l;
        
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    public static int recherche(){
        
        ArrayList<ArrayList<String>> liste= Lire.Lecture();
        
        // rechercheindice
        
        boolean trouver = false;
        
        int i= 3;
        
        int j=0;
        
        while ((! trouver) && i +1< liste.size()){
            
            
            
            System.out.println();
            
            System.out.print(i);
            
            System.out.println();
            
            
            
            while ((! trouver )&& j +1< liste.get(i).size() ){
                
                
                
                
                
                setCp(liste.get(i).get(j));
                
                setCc(liste.get(i).get(j+1));
                
                System.out.print(getCp());
                
                System.out.println();
                
                
                
                System.out.print(getCc());
                
                
                
                
                
                if (! (getCc().equals(getCp()) ) ){
                    
                    trouver=true;
                    
                }
                
                
                
                j=j+1;
                
            }
            
            i=i+1;
            
        }
        
        
        
        if ( trouver){
            
            System.out.println();
            
            
            
            return  i;
            
            
            
        }else{
            
            System.out.println();
            
            
            
            return -1;
            
        }
        
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    public static void affiche1 (ArrayList<Integer> tab){
        
        for(int j =0 ; j< tab.size() ;j++){
            
            System.out.print(tab.get(j)+ " ");
            
            
            
        }
        
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    public static void testforme(ArrayList<Integer> tab){
        
        boolean esttriangle=false;
        
        boolean estcercle=false;
        
        boolean estinconnue=false;
        
        int taille = tab.size();
        
        
        
        for(int j =0 ; j < tab.size();j++){
            
            
            
            if (taille !=0){
                
                taille=taille-1;}
            
            else{taille=0;}
            
            
            
            
            
            if ((tab.get(j)).equals(tab.get(taille))){
                
                
                System.out.println();
                
                estcercle=true;
                
            }
            
            else if((tab.get(j)).equals(tab.get(j +1 ))){
                
                estcercle=false;
                
            }
            
            else  if ((tab.get(j)) <= (tab.get(j +1 ))){
                
                esttriangle=true;
                
                estcercle=false;
                
            }
            
            else {
                
                estinconnue=true;
                
                esttriangle=false;
                
                estcercle=false;
                
            }
            
            
            
        }
        
        
        
        if (esttriangle){
            
            
            System.out.print("Forme de l'image : Triangle");
            System.out.println();

        }
        
        else if (estcercle){
            
            
            System.out.print("Forme de l'image : Cercle");
            System.out.println();

        }
        
        else if (estinconnue){
            
            
            System.out.print("Forme de l'image : Inconnue");
            System.out.println();

        }
        
        System.out.println();
        
    }
    
    
    
    
    
    
    
    public static String getCp() {
        
        return cp;
        
    }
    
    
    
    
    
    
    
    public static void setCp(String cp) {
        
        Figure.cp = cp;
        
    }
    
    
    
    
    
    
    
    public static String getCc() {
        
        return cc;
        
    }
    
    
    
    
    
    
    
    public static void setCc(String cc) {
        
        Figure.cc = cc;
        
    }
    
    
    
    
    
    
    
    
    
    public static void main (String[] args){
        
        //Lecture();
        
        
        
        descriptionimage();
        
        // System.out.print(  recherche());
        
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
}

