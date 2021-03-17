import javax.swing.JOptionPane;

public class Sorteo {
	public static void main(String[] args) {

		String [] plantel=new String[10];
	
		for (int i=0;i<10;i++){
		plantel[i]=JOptionPane.showInputDialog("Introduce jugador " + (i+1));
		}
		
		int cupo1 = (int)(Math.random()*10);
		
		int cupo2;
		do{
			cupo2 = (int)(Math.random()*10);
			}
		while (cupo2==cupo1);		
		if (cupo2!=cupo1){
			
		int cupo3;
		do{
			cupo3 = (int)(Math.random()*10);
			}
		while (cupo3==cupo1 || cupo3==cupo2);		
		if (cupo3!=cupo1 && cupo3!=cupo2){

		int cupo4;
		do{
			cupo4 = (int)(Math.random()*10);
		}
		while (cupo4==cupo3 || cupo4==cupo2 || cupo4==cupo1);		
		if (cupo4!=cupo1 && cupo4!=cupo2 && cupo4!=cupo3){
	
		int cupo5;
		do{
			cupo5 = (int)(Math.random()*10);
		}
		while (cupo5==cupo4 || cupo5==cupo3 || cupo5==cupo2 || cupo5==cupo1);		
		if (cupo5!=cupo1 && cupo5!=cupo2 && cupo5!=cupo3 && cupo5!=cupo4){
		
		int cupo6;
		do{
			cupo6 = (int)(Math.random()*10);
		}
		while (cupo6==cupo1 || cupo6==cupo2 || cupo6==cupo3 || cupo6==cupo4 || cupo6==cupo5);		
		if (cupo6!=cupo1 && cupo6!=cupo2 && cupo6!=cupo3 && cupo6!=cupo4 && cupo6!=cupo5){
		
		int cupo7;
		do{
			cupo7 = (int)(Math.random()*10);
		}
		while (cupo7==cupo1 || cupo7==cupo2 || cupo7==cupo3 || cupo7==cupo4 || cupo7==cupo5 || cupo7==cupo6);		
		if (cupo7!=cupo1 && cupo7!=cupo2 && cupo7!=cupo3 && cupo7!=cupo4 && cupo7!=cupo5 && cupo7!=cupo6){

		int cupo8;
		do{
			cupo8 = (int)(Math.random()*10);
		}
		while (cupo8==cupo1 || cupo8==cupo2 || cupo8==cupo3 || cupo8==cupo4 || cupo8==cupo5 || cupo8==cupo6 || cupo8==cupo7);		
		if (cupo8!=cupo1 && cupo8!=cupo2 && cupo8!=cupo3 && cupo8!=cupo4 && cupo8!=cupo5 && cupo8!=cupo6 && cupo8!=cupo7){
		
		int cupo9;
		do{
			cupo9 = (int)(Math.random()*10);
		}
		while (cupo9==cupo1 || cupo9==cupo2 || cupo9==cupo3 || cupo9==cupo4 || cupo9==cupo5 || cupo9==cupo6 || cupo9==cupo7 || cupo9==cupo8);		
		if (cupo9!=cupo1 && cupo9!=cupo2 && cupo9!=cupo3 && cupo9!=cupo4 && cupo9!=cupo5 && cupo9!=cupo6 && cupo9!=cupo7 && cupo9!=cupo8){
	
		int cupo10;
		do{
			cupo10 = (int)(Math.random()*10);
		}
		while (cupo10==cupo1 || cupo10==cupo2 || cupo10==cupo3 || cupo10==cupo4 || cupo10==cupo5 || cupo10==cupo6 || cupo10==cupo7 || cupo10==cupo8 || cupo10==cupo9);		
		if (cupo10!=cupo1 && cupo10!=cupo2 && cupo10!=cupo3 && cupo10!=cupo4 && cupo10!=cupo5 && cupo10!=cupo6 && cupo10!=cupo7 && cupo10!=cupo8 && cupo10!=cupo9){
			}
				
		System.out.println("Equipo A: ");
		System.out.println("");
		System.out.println(plantel[cupo1]);
		System.out.println(plantel[cupo2]);
		System.out.println(plantel[cupo3]);
		System.out.println(plantel[cupo4]);
		System.out.println(plantel[cupo5]);
		System.out.println("");
		System.out.println("Equipo B: ");
		System.out.println("");
		System.out.println(plantel[cupo6]);
		System.out.println(plantel[cupo7]);
		System.out.println(plantel[cupo8]);
		System.out.println(plantel[cupo9]);
		System.out.println(plantel[cupo10]);
		}
		}
		}
		}
		}
		}
		}
		}
	}
}