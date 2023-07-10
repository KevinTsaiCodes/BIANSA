%% BET.m -- Brain Extraction Toolbox in Matlab

clc;
close all;
clear all;
workspace;
format long g;
format compact;
fontSize = 12;

hasIPT = license('test', 'image_toolbox');
if ~hasIPT
  message = sprintf('Sorry, but you do not seem to have the Image Processing Toolbox.\nDo you want to try to continue anyway?');
  reply = questdlg(message, 'Toolbox missing', 'Yes', 'No', 'Yes');
  if strcmpi(reply, 'No')
    return;
  end
end

folder = '';

baseFileName = input('Enter the image filename (e.g., image.jpg): ', 's');
fullFileName = fullfile(folder, baseFileName);
% Check if file exists.
if ~exist(fullFileName, 'file')
  fullFileNameOnSearchPath = baseFileName;
  if ~exist(fullFileNameOnSearchPath, 'file')
    errorMessage = sprintf('Error: %s does not exist in the search path folders.', fullFileName);
    uiwait(warndlg(errorMessage));
    return;
  end
end
grayImage = imread(fullFileName);
[rows, columns, numberOfColorBands] = size(grayImage);
if numberOfColorBands > 1
  grayImage = grayImage(:, :, 2);
end
subplot(2, 3, 1);
imshow(grayImage, []);
axis on;
title('Original Grayscale Image', 'FontSize', fontSize);
set(gcf, 'Units', 'Normalized', 'OuterPosition', [0 0 1 1]);
set(gcf, 'Name', 'Demo by ImageAnalyst', 'NumberTitle', 'Off')
[pixelCount, grayLevels] = imhist(grayImage);
subplot(2, 3, 2);
bar(grayLevels, pixelCount);
grid on;
title('Histogram of original image', 'FontSize', fontSize);


xlim([0 grayLevels(end)]);
grayImage = grayImage(3:end-3, 4:end-4);
binaryImage = grayImage > 20;
binaryImage = bwareaopen(binaryImage, 10);
subplot(2, 3, 3);
imshow(binaryImage, []);
axis on;
title('Binary Image', 'FontSize', fontSize);

binaryImage(end,:) = true;
binaryImage = imfill(binaryImage, 'holes');
subplot(2, 3, 4);
imshow(binaryImage, []);
axis on;
title('Cleaned Binary Image', 'FontSize', fontSize);


se = strel('disk', 15, 0);
binaryImage = imerode(binaryImage, se);
subplot(2, 3, 5);
imshow(binaryImage, []);
axis on;
title('Eroded Binary Image', 'FontSize', fontSize);


finalImage = grayImage;
finalImage(~binaryImage) = 0;
subplot(2, 3, 6);
imshow(finalImage, []);
axis on;
title('Skull stripped Image', 'FontSize', fontSize);
msgbox("The brain extration operation has been successfully completed","Success");

[filepath, name, ~] = fileparts(baseFileName);

newFilename = fullfile(filepath, [name, '_brain.png']);

imwrite(finalImage, newFilename);

clc;
clear all;
