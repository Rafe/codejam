import java.lang.*;
import java.util.*;


public class Question7{
  ArrayList<HtWt> items;
  ArrayList<HtWt> lastFoundSeq;
  ArrayList<HtWt> maxSeq;

  ArrayList<HtWt> seqWithMaxLength(ArrayList<HtWt> seq1,ArrayList<HtWt> seq2){
    return seq1.size() > seq2.size() ? seq1 : seq2;
  }


}
