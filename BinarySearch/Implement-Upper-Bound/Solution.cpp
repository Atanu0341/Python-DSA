int upperBound(vector<int> &arr, int x, int n){
	// Write your code here.	
	int start = 0;
	int end = n -1;
	int ans = n;

	int mid = start + (end - start)/2;

	while(start<=end){

		if(arr[mid]>x){
			ans = mid;
			end = mid - 1;
		}
		else{
			start = mid + 1;
		}
		mid = start + (end - start)/2;
	}
	return ans;
}