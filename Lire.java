
import java.io.*;

public class Lire {
public String fichier ;
	

	
	public Lire() {
		fichier=null;
		}
	
	public Lire(String fichiers ) {
		this.fichier=fichiers;
		}
	
	public String getFile(){
		return fichier;
	}
	
	
	
	
///////////////////////////////////////////////////////////////////////////////////////////////
//	LIRE 
//////////////////////////////////////////////////////////////////////////////////////////////
	public static void main (String[] args) {
		// On ouvre l'entrÃ©e standard
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// uneLigne va stocker la ligne lue
		String uneLigne = null;
		// CONTINUER indique s'il y a encore des choses Ã  lire ou si on a terminÃ©.
		boolean continuer = true;
		while ( continuer ) {
			try {
				uneLigne = br.readLine();
				if ( uneLigne != null ) {
					// On affiche chaque ligne lue
					System.out.println( "-->" + uneLigne + "<--" );
					// on supprime les espaces multiples
					uneLigne.replaceAll( "\\s+", " " ); 
					// On va maintenant la rÃ©afficher en sÃ©parant les mots.
					System.out.print( "|" );
					for ( String s : uneLigne.split( " " ) ) {
						if ( s.length() > 0 ) {
							System.out.print( s + "|" );
						}
					}
					System.out.println( "" );
				} else {
					continuer = false;
				}
			} catch (IOException ioe) {
				System.out.println( "Erreur de lecture" );
				System.exit(1);
			}
		}
	}

///////////////////////////////////////////////////////
// ANALYSE D'IMAGE
	


	
	
	
	
	
	
	
	
	
	


}