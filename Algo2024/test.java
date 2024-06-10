class Solutions{
    public int subarraydivbyk(int[] arr, int k){
        int count = 0;
        int[] prefix = new int[k];
        prefix[0]= 1;
        int prefixsum = 0; 
        for (int i :arr){
            prefixsum+= i;
            int mod = ((prefixsum%k) + k)%k;
            prefix[mod]++;
        }
        for (int i : prefix){
            count += (i * (i-1) )/ 2;
        }
        return count;
    }

    public static void main(String[] args) {
        int[] arr = new int[] {4,9,0,-2,-3,1};
        int k = 5;
        Solutions S= new Solutions()
        System.out.println(S.subarraydivbyk(arr,k));



    }
}
