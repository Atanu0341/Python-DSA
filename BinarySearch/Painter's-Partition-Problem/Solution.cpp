bool isPossible(vector<int> &boards , int k, int mid){

    int paintCount = 1;

    int boardSum = 0;

 

    for(int i=0 ; i<boards.size() ; i++){

        if (boardSum + boards[i] <= mid) {

            boardSum+=boards[i];

        }

        else{

            paintCount++;

            if(paintCount>k || boards[i]>mid){

                return false;

            }

            boardSum = boards[i];

        }

    }

    return true;

}

 

int findLargestMinDistance(vector<int> &boards, int k)

{

    int s=0;

    int sum = 0;

    int ans=-1;

    for(int i = 0; i<boards.size(); i++){

        sum+=boards[i];

    }

    int e = sum;

    int mid= s+(e-s)/2;

    while(s<=e){

        if(isPossible(boards , k , mid)){

            ans=mid;

            e=mid-1;

        }

        else{

            s=mid+1;

        }

        mid= s+(e-s)/2;

    }

    return ans;

}

