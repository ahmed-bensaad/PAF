imps=imread('/cal/homes/abensaad/Desktop/PAF/PAF/visual10');
imre=imread('/cal/homes/abensaad/Desktop/PAF/PAF/visual1');


%Nombre de pixels faisant 5Km pour chaque image. 
 x=floor(25/3);
 y=floor(25/5);

%prise de sous partie des images
T=imre(1:500,5000-500+1:5000,1:3);
U=imps(1:800,8000-800+1:8000,1:3);




A=T;
D=U;
S=U;
A(:,:,:)=0;
D(:,:,:)=0;
S(:,:,:)=0;

A=fftshift(fft2(T));
D=padarray(A,[150,150]);
S=uint8((ifft2(D)));

figure(1);imshow(U);

figure(2);imshow(real(S));
figure(3);imshow(real(T));
