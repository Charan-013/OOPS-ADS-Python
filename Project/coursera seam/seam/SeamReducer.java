import edu.princeton.cs.algs4.Picture;

public class SeamReducer {
    private int imgWidth;
    private int imgHeight;
    private Picture imgCopy;

    public SeamReducer(Picture sourceImg) {
        if (sourceImg == null) {
            throw new IllegalArgumentException("null image input");
        }

        imgCopy = new Picture(sourceImg);
        imgWidth = sourceImg.width();
        imgHeight = sourceImg.height();
    }

    public Picture image() {
        return new Picture(imgCopy);
    }

    public int width() {
        return imgWidth;
    }

    public int height() {
        return imgHeight;
    }

    public double getEnergy(int cx, int cy) {
        verifyCol(cx);
        verifyRow(cy);

        if (cx == 0 || cx == imgWidth - 1 || cy == 0 || cy == imgHeight - 1) {
            return 1000;
        }

        int upper = imgCopy.getRGB(cx, cy - 1);
        int lower = imgCopy.getRGB(cx, cy + 1);
        int left = imgCopy.getRGB(cx - 1, cy);
        int right = imgCopy.getRGB(cx + 1, cy);
        double yGrad = pixelGradient(upper, lower);
        double xGrad = pixelGradient(left, right);

        return Math.sqrt(xGrad + yGrad);
    }

    private double pixelGradient(int p1, int p2) {
        int r1 = (p1 >> 16) & 0xFF;
        int g1 = (p1 >> 8) & 0xFF;
        int b1 = (p1 >> 0) & 0xFF;
        int r2 = (p2 >> 16) & 0xFF;
        int g2 = (p2 >> 8) & 0xFF;
        int b2 = (p2 >> 0) & 0xFF;

        return Math.pow(r1 - r2, 2) + Math.pow(g1 - g2, 2) + Math.pow(b1 - b2, 2);
    }

    public int[] verticalPath() {
        double[][] energMap = new double[imgWidth][imgHeight];
        for (int r = 0; r < imgHeight; r++) {
            for (int c = 0; c < imgWidth; c++) {
                energMap[c][r] = getEnergy(c, r);
            }
        }

        int[][] edgeTracker = new int[imgWidth][imgHeight];
        double[][] distTracker = new double[imgWidth][imgHeight];

        for (int r = 0; r < imgHeight; r++) {
            for (int c = 0; c < imgWidth; c++) {
                distTracker[c][r] = Double.POSITIVE_INFINITY;
                if (r == 0) distTracker[c][r] = energMap[c][r];
            }
        }

        for (int r = 0; r < imgHeight - 1; r++) {
            for (int c = 0; c < imgWidth; c++) {
                if (distTracker[c][r + 1] > distTracker[c][r] + energMap[c][r + 1]) {
                    distTracker[c][r + 1] = distTracker[c][r] + energMap[c][r + 1];
                    edgeTracker[c][r + 1] = c;
                }
                if (c - 1 > 0 && distTracker[c - 1][r + 1] > distTracker[c][r] + energMap[c - 1][r + 1]) {
                    distTracker[c - 1][r + 1] = distTracker[c][r] + energMap[c - 1][r + 1];
                    edgeTracker[c - 1][r + 1] = c;
                }
                if (c + 1 < imgWidth && distTracker[c + 1][r + 1] > distTracker[c][r] + energMap[c + 1][r + 1]) {
                    distTracker[c + 1][r + 1] = distTracker[c][r] + energMap[c + 1][r + 1];
                    edgeTracker[c + 1][r + 1] = c;
                }
            }
        }

        int lowestCol = 0;
        double minPathCost = Double.POSITIVE_INFINITY;
        for (int c = 0; c < imgWidth; c++) {
            if (distTracker[c][imgHeight - 1] < minPathCost) {
                minPathCost = distTracker[c][imgHeight - 1];
                lowestCol = c;
            }
        }

        int[] seamLine = new int[imgHeight];
        int trackRow = imgHeight - 1;
        while (trackRow >= 0) {
            seamLine[trackRow] = lowestCol;
            lowestCol = edgeTracker[lowestCol][trackRow--];
        }

        return seamLine;
    }

    public int[] horizontalPath() {
        rotateImage();
        int[] seam = verticalPath();
        rotateImage();
        return seam;
    }

    public void removeVertical(int[] line) {
        if (line == null) throw new IllegalArgumentException("null seam");
        if (line.length != imgHeight) throw new IllegalArgumentException("seam length mismatch");
        verifyPath(line);
        if (imgWidth <= 1) throw new IllegalArgumentException("image width too small");

        Picture resized = new Picture(imgWidth - 1, imgHeight);
        for (int r = 0; r < imgHeight; r++) {
            for (int c = 0; c < imgWidth - 1; c++) {
                verifyCol(line[r]);
                if (c < line[r]) {
                    resized.setRGB(c, r, imgCopy.getRGB(c, r));
                } else {
                    resized.setRGB(c, r, imgCopy.getRGB(c + 1, r));
                }
            }
        }
        imgCopy = resized;
        imgWidth--;
    }

    public void removeHorizontal(int[] line) {
        if (line == null) throw new IllegalArgumentException("null seam");
        if (line.length != imgWidth) throw new IllegalArgumentException("seam length mismatch");
        verifyPath(line);
        if (imgHeight <= 1) throw new IllegalArgumentException("image height too small");

        rotateImage();
        removeVertical(line);
        rotateImage();
    }

    private void rotateImage() {
        Picture temp = new Picture(imgHeight, imgWidth);
        for (int r = 0; r < imgWidth; r++) {
            for (int c = 0; c < imgHeight; c++) {
                temp.setRGB(c, r, imgCopy.getRGB(r, c));
            }
        }
        imgCopy = temp;
        int swap = imgHeight;
        imgHeight = imgWidth;
        imgWidth = swap;
    }

    private void verifyCol(int col) {
        if (col < 0 || col > imgWidth - 1) {
            throw new IllegalArgumentException("invalid column index");
        }
    }

    private void verifyRow(int row) {
        if (row < 0 || row > imgHeight - 1) {
            throw new IllegalArgumentException("invalid row index");
        }
    }

    private void verifyPath(int[] path) {
        for (int i = 0; i < path.length - 1; i++) {
            if (Math.abs(path[i] - path[i + 1]) > 1) {
                throw new IllegalArgumentException("non-contiguous seam");
            }
        }
    }
}
