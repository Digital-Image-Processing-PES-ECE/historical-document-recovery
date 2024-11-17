img = imread(<image_path>); 

if size(img, 3) == 3
    grayImg = rgb2gray(img);
else
    grayImg = img;
end

denoisedImg = imgaussfilt(grayImg, 0.5);

claheImg = adapthisteq(denoisedImg, 'ClipLimit', 0.01, 'NumTiles', [8 8]);

T = adaptthresh(claheImg, 0.45, 'ForegroundPolarity', 'dark', 'NeighborhoodSize', [25 25]);
binaryImg = imbinarize(claheImg, T);

finalEnhancedText = imadjust(uint8(binaryImg) * 255);

figure;
subplot(2, 3, 1);
imshow(img);
title('Original Image');

subplot(2, 3, 2);
imshow(grayImg);
title('Grayscale Image');

subplot(2, 3, 3);
imshow(denoisedImg);
title('Denoised (Gaussian Filter)');

subplot(2, 3, 4);
imshow(claheImg);
title('CLAHE Enhanced');

subplot(2, 3, 5);
imshow(binaryImg); 
title('Adaptive Thresholding (Sauvola)');

subplot(2, 3, 6);
imshow(finalEnhancedText);
title('Final Enhanced Image');
