using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PrimerWindowsForm
{
    public partial class Form1 : Form
    {
        double numero =0;
        double digito =0;
        double segundo = 0;
        double primero = 0;
        string operador=null;
        bool sw = true;
        public Form1()
        {
            InitializeComponent();
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
  
         
            digito = Convert.ToDouble(((Button)sender).Text);
            numero = numero * 10 + digito;
            textBox1.Text = numero.ToString();
            sw = true;

        }


        private void Form1_Load_1(object sender, EventArgs e)
        {
            numero = 0;
        }

        private void buttonLimpiar_Click(object sender, EventArgs e)
        {
            numero = 0;
            textBox1.Text = "";
            segundo = 0;
            primero = 0;
            label1.Text = "";
            sw = true;
        }

        private void buttonIgual_Click(object sender, EventArgs e)
        {
            try
            {
                
                segundo = Convert.ToDouble(textBox1.Text);   
            }
            catch (Exception )
            {
                segundo = 0;
            }
            label1.Text += textBox1.Text;
            double suma, resta, mul, div;
            if (sw)
            {
                sw = false;
                if (operador != null)
                {
                    switch (operador)
                    {
                        case "+":
                            suma = Suma(primero, segundo);
                            textBox1.Text = suma.ToString();
                            break;
                        case "-":
                            resta = Resta(primero, segundo);
                            textBox1.Text = resta.ToString();
                            break;
                        case "x":
                            mul = Multiplicacion(primero, segundo);
                            textBox1.Text = mul.ToString();
                            break;
                        case "/":
                            div = Divicion(primero, segundo);
                            textBox1.Text = div.ToString();
                            break;

                    }
                }
                else
                {
                    numero = 0;
                }
            }
            


        }
        private void buttonOperador_Click(object sender, EventArgs e)
        {
            //todo la logica de calculadora
            operador = ((Button)sender).Text;
            primero = Convert.ToDouble(textBox1.Text);
            numero = 0;
            label1.Text = textBox1.Text +" "+((Button)sender).Text;
            textBox1.Clear();

        }
        private double Suma(double a, double b)
        {
            try
            {
                double s = 0;
                return s = a + b;
            }
            catch (Exception e)
            {
                return 0;
            }
            
        }

        private double Resta(double a,double b)
        {
            try
            {
                double s = 0;
                return s = a - b;
            }
            catch (Exception e)
            {
                return 0;
            }
        }
        private double Multiplicacion(double a, double b)
        {
            try
            {
                double s = 0;
                return s = a * b;
            }
            catch (Exception e)
            {
                return 0;
            }
        }
        private double Divicion(double a, double b)
        {
            try
            {
                double s = 0;
                return s = a / b;
            }
            catch (Exception e)
            {
                return 0;
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
