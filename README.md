# Driver_LED_Raspberry
Repositório para armazenar o passo a passo para rodar um driver para acender um led a partir de um script em python.

![image](https://github.com/VictorRavani/Driver_LED_Raspberry/assets/101602056/0a0a3c0b-33d3-4f57-babc-1e1099cf97ac)

Versão: Linux raspberrypi 6.1.21-v7+ #1642 SMP Mon Apr  3 17:20:52 BST 2023 armv7l GNU/Linux

Obs.: Ignore a placa de desenvolvimento da ST e os demais periféricos que não fazem parte deste teste. 

#Instalando drive na Raspberry para rodas um script em Python

- Descompacte a pasta em um local do seu Raspberry.
Obs.: Os comandos devem ser escritos no prompt de comando do próprio Raspberry 
Imagem de exemplo:

![image](https://github.com/VictorRavani/Driver_LED_Raspberry/assets/101602056/9daa600f-2de1-4031-9e3a-0c7d90931fc5)

- Acesse o local do arquivo: 
Exemplo: cd /home/eletronica/Documentos/Aulas_POS/16_03_24/01-LED_DRIVER           
- Instale o drive na Raspberry conforme as instruções do Arquivo COMANDOS_UTILIZADOS.txt

![image](https://github.com/VictorRavani/Driver_LED_Raspberry/assets/101602056/012449bc-8acc-4e42-b068-f105ba1083a8)


- Depois copei e cole o scrip em python (programa) no mesmo local da pasta 01-LED_DRIVER (junto com os arquivos Makefile e etc.
- Execute o script:
Exemplo: python pisca.py   m          

![image](https://github.com/VictorRavani/Driver_LED_Raspberry/assets/101602056/36827178-cef9-4588-affa-15ae1b7cfa3a)

