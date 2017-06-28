imre=imread('/cal/homes/abensaad/Desktop/PAF/PAF/visual1');

imps=imread('/cal/homes/abensaad/Desktop/PAF/PAF/visual10');



T=imre(1:500,5000-500+1:5000,1:3);
U=imps(1:800,8000-800+1:8000,1:3);
%prise de sous partie des images

 
%imshow(T);
 
%
% s1=recalage_gray(T(:,:,1));
% s2=recalage_gray(T(:,:,2));
% s3=recalage_gray(T(:,:,3));
%
% a(:,:,1)=s1;
% a(:,:,2)=s2;
% a(:,:,3)=s3;
%
% figure();
% imshow(a);
 
 
 
A(:,:,1)=fftshift(fft2(double(T(:,:,1))));
A(:,:,2)=fftshift(fft2(double(T(:,:,2))));
A(:,:,3)=fftshift(fft2(double(T(:,:,3))));
 
D(:,:,1)=padarray(A(:,:,1),[150,150]);
D(:,:,2)=padarray(A(:,:,2),[150,150]);
D(:,:,3)=padarray(A(:,:,3),[150,150]);

 
 
S(:,:,1)=ifft2(fftshift(D(:,:,1)));
S(:,:,2)=ifft2(fftshift(D(:,:,2)));
S(:,:,3)=ifft2(fftshift(D(:,:,3)));
 
[nx,ny,nz]=size(T);
S=S/nx/ny;
 
[nx,ny,nz]=size(S);
S=S*nx*ny;
 
 
 
figure(1);
imshow(uint8(abs(S)));
figure(2);
imshow(U);
figure(3);
imshow(abs(uint8(abs(S))-U));
 
 
 
 
 
 
 
%imagesc(real(S));
% figure(2);imagesc(double(log(abs((AA)))));
% figure(3);imshow(real(T));
