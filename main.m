system('python main.py')
i=0;
T=zeros(1,100);
while (exist(strcat('image',num2str(i),'.tif'),'file')~=0)
T(i)=imread(strcat('image',num2str(i),'.tif'));
i=i+1;
end
