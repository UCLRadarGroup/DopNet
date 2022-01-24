
%This part is getting the directory where your Matlab is running right now
dir=pwd;
%This parts loads the data
Person= 'A'% Choose the person letter
load([dir,'\','Data_Per_PersonData_Training_Person_',Person,'.mat'])

Gesture = 1; % Choose one of the Gestures which are in this order: 'Wave' =1,'Pinch'=2,'Swipe'=3,'Click' =4

Repeat = 17; % Choose one of the measurements

x = Data_Training.Doppler_Signals{Gesture}{Repeat}; %Get The data




 figure;imagesc(20*log10(abs(x)./max(abs(x(:)))),[-30,0])
