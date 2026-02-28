// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html

class PeekingIterator implements Iterator<Integer> {

    private List<Integer> nums;
    private int i;

	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
        nums = new ArrayList<>();
        while (iterator.hasNext()) {
            nums.add(iterator.next());
        }  
        i = 0;
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        return nums.get(i);
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
        return nums.get(i++);
	}
	
	@Override
	public boolean hasNext() {
        return i < nums.size();
	}
}