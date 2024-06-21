int lowerBound(vector<int> arr, int n, int x) {
	// Write your code here
	if(arr[0]>=x){
        return 0;
    }
	else if(arr[n-1]<x){
        return n;
    }

	int start = 0;
	int end = n-1;
	
	int mid = start + (end - start)/2;

	while(start<=end){

		if(arr[mid]==x){
			return mid;
		}
		else if(arr[mid]<x){
			start = mid + 1;
		}
		else{
			end = mid - 1;
		}
		mid = start + (end - start)/2;
	}
	return start;
}


// or

int lowerBound(vector<int> arr, int n, int x) {
	int low = 0, high = n - 1;
    int ans = n;
    

    while (low <= high) {
        int mid = low + (high - low)/2;
        // maybe an answer
        if (arr[mid] >= x) {
            ans = mid;
            //look for smaller index on the left
            high = mid - 1;
        }
        else {
            low = mid + 1; // look on the right
        }
    }
    return ans;

}
