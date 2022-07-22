package b.b19;

import java.util.ArrayList;

public class Question {

	String libellé;
	ArrayList<Réponse> réponses;
	
	public Question(String l) {
		this.libellé = l;
		this.réponses = new ArrayList<>();
	}
	
	public void ajouterRéponse(Réponse r) {
		this.réponses.add(r);
	}
	
	public String toString() {
		String out = this.libellé +"\n";
		for (int i=0; i<this.réponses.size(); i++) {
			out += (i+1) + ") " + this.réponses.get(i).libellé + "\n";
		}
		return out;
	}
	
	public static void main(String[] args) {

		Question q0 = new Question("Quelle est la hauteur de la tour eiffel ?"); 
		q0.ajouterRéponse(new Réponse("405 mètres", false));
		q0.ajouterRéponse(new Réponse("300 mètres", true));
		q0.ajouterRéponse(new Réponse("1,2 kilomètres", false));
		q0.ajouterRéponse(new Réponse("405 centimètres", false));
		
		System.out.println(q0);
	}

}
