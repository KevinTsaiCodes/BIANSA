clc;
clear all;

hasIPT = license('test', 'image_toolbox');
if ~hasIPT
    message = sprintf('Sorry, but you do not seem to have the Image Processing Toolbox.\nDo you want to try to continue anyway?');
    reply = questdlg(message, 'Toolbox missing', 'Yes', 'No', 'Yes');
    if strcmpi(reply, 'No')
        return;
    end
end

inputFolder = uigetdir('', 'Select Input Image Directory');
outputFolder = uigetdir('', 'Select Output Directory');

if isempty(inputFolder) || isempty(outputFolder)
    return; % User clicked Cancel or didn't select a folder
end

imageFiles = dir(fullfile(inputFolder, '*.png')); % Assuming images are in PNG format. Modify if using different format.

for fileIdx = 1:length(imageFiles)
    baseFileName = imageFiles(fileIdx).name;
    fullFileName = fullfile(inputFolder, baseFileName);
    grayImage = imread(fullFileName);
    [rows, columns, numberOfColorBands] = size(grayImage);
    if numberOfColorBands > 1
        grayImage = grayImage(:, :, 2);
    end
    
    grayImage = grayImage(3:end-3, 4:end-4);
    binaryImage = grayImage > 20;
    binaryImage = bwareaopen(binaryImage, 10);
    
    binaryImage(end,:) = true;
    binaryImage = imfill(binaryImage, 'holes');
    
    se = strel('disk', 15, 0);
    binaryImage = imerode(binaryImage, se);
    
    finalImage = grayImage;
    finalImage(~binaryImage) = 0;
    
    desiredSize = [512, 512];
    finalImage = imresize(finalImage, desiredSize);
    
    [~, name, ~] = fileparts(baseFileName);
    newFilename = fullfile(outputFolder, [name, '_brain.png']);
    imwrite(finalImage, newFilename);
end

clc;
clear all;
