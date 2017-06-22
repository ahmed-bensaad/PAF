system('python /cal/homes/abensaad/Desktop/PAF/PAF/main.py')
i=1;
ch='1';
ch1=strcat('/cal/homes/abensaad/Desktop/PAF/PAF/image','1');
while (exist(ch1,'file')~=0)
imread(ch1);
i=i+1;
ch=num2str(i);
ch1=strcat('/cal/homes/abensaad/Desktop/PAF/PAF/image',ch);
end
