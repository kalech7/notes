cordenadas de 
* cordenadas de posicion -1 a 1 
* color 0 a 1
fuera de estos rangos no se ve el color
* texturas 0 a 1 cuando saale del rango se llama texture wrapping lo que sucede es que se puede configurar (gl repeat,mirrored ,edge,clamp to border)
a los pixeles de las texturas se llaman texel
### texture filteting
cuando la textura es mas grnde que los frangmentos se llama mignification donde se deben reducira a pocos pixeles (zoom out)
pasar de pocos texeles a varios pixeles se llama magnification (zoom in)

### Algoritmo
nearest (vecino mas cercano) utiliza el texel mas cercano y uno y luego lo borra 
Linear se mezclan lsos texeles donde se hace una interpolation bilinear 

texel swimming
la iamgen se empieza a distorcionar cuando se mignifica  esto se soluciona mipmaps (se prefieren las imagenes en imagenes mas pequeñas ya vienen calculadas ) solo se usa mipmaps cuando se tienen mignification 
en jpg tiene 3 canles rgb
en png 4 canales 
este datos esta guardado en la memoria del cpu 
