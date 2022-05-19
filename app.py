import streamlit as st
st.title("Seleccionador de alimentos")
st.write("Sólo necesitas seleccionar los ingredientes que no quieres consumir en tu platillo favorito")
st.image("https://www.milenio.com/uploads/media/2021/11/16/comida-mexicana.jpg")
st.sidebar.title("Te mostraremos los platillos que no tengan tu ingrediente indeseado")
st.write("Bebidas")
st.write("Agua de horchata")
with st.expander("Ingredientes"):
  st.write("Arroz, canela, agua, azucar, vainilla, leche")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMUs923wSi91HnTOWMMC0Sb-olTh--j526Ig&usqp=CAU")


#st.write('Escogiste',  option)
st.write("Agua de guayaba")
with st.expander("Ingredientes"):
  st.write ("Agua, guayaba, azucar")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRM_Z2N_Ib7MSQGy7fuLo-YwGIiz-pjlR9AfA&usqp=CAU")
ingredientes= st.multiselect('¿Qué ingrediente deseas descartar?',
     ['agua', 'azucar', 'guayaba'], 
                 ['azucar'])
st.write("tu bebida sin:",ingredientes)
st.write("Platillos")
st.write("Enchiladas verdes")
with st.expander("Ingredientes"):
  st.write("tortillas, salsa verde, cebolla, queso, lechuga, crema")
  st.image("https://dam.cocinafacil.com.mx/wp-content/uploads/2020/06/flautas-de-pollo-con-salsa-de-aguacate-1170x655.jpg")
ingredientes= st.multiselect('¿Qué ingrediente deseas descartar?',
     ["tortillas", "salsa verde", "cebolla", "queso", "lechuga", "crema", "salsa roja"], 
                 ["cebolla"])
st.write("tu platillo sin:",ingredientes)
st.write("Pozole")
with st.expander("Ingredientes"):
  st.write("carne de puerco", "maiz", "rábanos" , "lechuga", "salsa roja", "salsa verde", "aguacate")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRGNPuO6_DFj_2NXerUP5Od6oV6hW8uM4_1A&usqp=CAU")
ingredientes= st.multiselect("¿Qué ingrediente deseas descartar?",
     ["salsa verde", "lechuga", "carne de puerco", "maiz", "rábanos", "salsa roja", "aguacate"], 
                 ["rábanos"])
st.write("tu platillo sin:",ingredientes)
st.write("Tamales")
with st.expander("Ingredientes"):
  st.write("carne de puerco", "masa a base de maiz", "salsa roja", "salsa verde")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3Uw5bjw2dMceU3qO0zib1HIYJjEuL5KtqjA&usqp=CAU")
st.multiselect('¿Qué ingrediente deseas descartar?',
     ["salsa verde", "carne de puerco", "salsa roja", "masa a base de maiz"], 
                 ["salsa roja"])
st.write("Chiles rellenos capeados")
with st.expander("Ingredientes"):
 st.write("Chile chilaca", "queso", "cubierta de huevo", "frijoles", "arroz")
 st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCpPSeFk8j_EtGLFONF2-UhBJnG0D5nowI8Q&usqp=CAU")
  
st.multiselect("¿Qué ingrediente deseas descartar?",
     ["queso", "cubierta de huevo", "arroz", "frijoles"],
                    ["queso"])
st.write("Entradas") 
st.write("Guacamole con totopos")
with st.expander("Especificaciones"):
  st.write("Totopos sin ajo", "Totopos con ajo")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9xo1_UmO6E40Q7QA22QqDhBIvO6FkSKF3uA&usqp=CAU")
  option = st.selectbox('Totopos: Con ajo , Sin ajo',('Con ajo', 'Sin ajo'))
st.write('Escogiste totopos',  option)
st.title("Postres")
st.write("Pan dulce")
with st.expander("Especificaciones"):
  st.write("Conchitas,","Quequis,","Puerquito,","Beso" )
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTby-Yha-b3tVmaIgIllL25xAJDrU8F1-P8SA&usqp=CAU")
  option = st.selectbox('Conchitas,Quequis,Puerquito,Beso',('Conchitas', 'Quequis','Puerquito','Beso'))
st.write('Escogiste',  option)
