image = imread('./sourceImg1.jpg');
imshow(image)
size(image)
[x,y] = ginput(4)

fp = fopen('./coord.txt', 'w');
fprintf(fp,'%.2f,%.2f\n',[x,y])