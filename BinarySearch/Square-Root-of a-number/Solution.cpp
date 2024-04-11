long long int binarySearch(int num){
        int start = 0;
        int end = num;
        long long int mid = start + (end-start)/2;
        int ans = -1;

        while(start<=end){

            long long int square = mid * mid;

            if(square == num){
                return mid;
            }

            else if(square < num){
                ans = mid;
                start = mid+ 1;
            }
            //sqaure>num
            else{
                end = mid - 1;
            }
            mid = start + (end-start)/2;
        }
        return ans;
    }

int floorSqrt(int n)
{
    // Write your code here.
    return binarySearch(n);
}
