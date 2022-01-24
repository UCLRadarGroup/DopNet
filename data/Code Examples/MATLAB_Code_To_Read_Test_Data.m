

%This part is getting the directory where your Matlab is running right now
dir=pwd;
%This parts loads the data
load([dir,'\','Data_For_Test.mat'])

% Choose one of the measurements
Repeat = input('Please tell me repeat number: ');


%Get The data
x = Data_rand{Repeat,1}{1,1}; 

% plot the data to see how it looks like
 figure;imagesc(20*log10(abs(x)./max(abs(x(:)))),[-30,0]) 
