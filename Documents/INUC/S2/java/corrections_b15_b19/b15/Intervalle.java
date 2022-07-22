package b.b15;

public class Intervalle {

	private int borneMin, borneMax;
	
	public Intervalle(int a, int b) {
		this.borneMin = a;
		this.borneMax = b;
	}
	
	public boolean contient(int v) {
		return v>=this.borneMin && v<=this.borneMax;
	}
	
	public static void main(String[] args) {
		
		Intervalle i = new Intervalle(3,7);
		System.out.println(i.contient(1));
		System.out.println(i.contient(4));
	}

}
