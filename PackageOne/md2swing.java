package PackageOne;

import javax.swing.*;

import java.awt.event.*;
import java.util.ArrayList;

public class md2swing {
	
     md2swing() {
        JFrame f= new JFrame("Homework");
        
        JButton add = new JButton("Add");  
        add.setBounds(90,60,70,30);  
        
        JButton run = new JButton("Run");  
        run.setBounds(165,60,70,30);
        
        JButton delete = new JButton("Delete");
        delete.setBounds(90, 320, 70, 30);
        
        JButton clear = new JButton("Clear");
        clear.setBounds(165, 320, 70, 30);
        
        final DefaultListModel<String> l1 = new DefaultListModel<>(); 
     
          final JList<String> list1 = new JList<>(l1);  
          list1.setBounds(10,100,150,210);  
          
          DefaultListModel<String> l2 = new DefaultListModel<>();  
      
         
          final JList<String> list2 = new JList<>(l2);  
          list2.setBounds(165,100,150,210);  
          
          JTextField t1;  
          t1=new JTextField("");  
          t1.setBounds(15,25,300,25);  
          f.add(list1); f.add(list2); f.add(add); f.add(run); f.add(delete); f.add(clear); f.add(t1);
          f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);    
          f.setSize(340,400);  
          f.setLayout(null);  
          f.setVisible(true);
          f.setLocationRelativeTo(null);
          
          add.addActionListener(new ActionListener() {  
        	  
              public void actionPerformed(ActionEvent e) { 
            	             	  
            	  l1.addElement(t1.getText());
                 
              }  
           }); 
          
          run.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {

				for(int i = 0; i < l1.size();i++) {
					String [] s = l1.get(i).split("\\s+");
					ArrayList<String> fragments = new ArrayList<String>();
					
					for(String f: s) {
						fragments.add(f + " " + f);
	
					}
					
					l2.addElement(String.join(" ", fragments));
				}
			}
          });
          
          delete.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				
				l1.clear();
				
			}
        	  
          });
          
          clear.addActionListener(new ActionListener() {

  			@Override
  			public void actionPerformed(ActionEvent e) {
  				
  				l2.clear();
  				
  			}
          	  
            });
       
     }  
public static void main(String args[])  {  
	
   System.out.println("Alina Verkholomova");
   new md2swing();
    }}  