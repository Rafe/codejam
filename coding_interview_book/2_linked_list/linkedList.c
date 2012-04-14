#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

#define True 1
#define False 0
#define TEST 1
#define DATA_MAX 80
#define indexOutOfRange(list,index) (index < 0 || index >= list->length)
#define isEmpty(list) (list ==NULL || list->length == 0)
typedef struct node{
  char *data;
  struct node* next;
} Node;

typedef struct linkedList{
  int length;
  Node* top;
  Node* current;
} LinkedList;

int add(LinkedList* list,char* data);
int displayList(LinkedList* list);
int find(LinkedList* list,char* text);
void sort(LinkedList* list);
char* get(LinkedList* list,int index);
Node* createNode(char* data);
LinkedList* createList();
void destory(LinkedList* list);
void testSuite();
void usage();
char* get_input(char* buffer);

int main(int argc, char* argv[]){
  int input = 1,index = 0,pos = 0;
  char c,*temp,*buffer = (char*) calloc(DATA_MAX,sizeof(char));
  LinkedList *list = createList();
#ifdef TEST
  testSuite();
#endif
  usage();
  while(input != 0){
    input = -1;
    printf("please enter command (0-5, or u for usage )\n> ");
    scanf("%d", &input);
    switch(input){
      case 0:
        //input = 0;
        printf("exit program...\n");
        break;
      case 1: //add
        printf("please enter the data you want to add\n> ");
        temp = get_input(buffer);
        add(list,temp);
        displayList(list);
        break;
      case 2: //get
        printf("please input the index number:\n> ");
        scanf("%d",&index);
        printf("%d :: %s\n",index,get(list,index));
        break;
      case 3: //insert
        printf("please input the data you want to insert\n> ");
        temp = get_input(buffer);
        printf("please input the index you want to insert\n> ");
        scanf("%d",&index);
        insert(list,index,temp);
        displayList(list);
        break;
      case 4: //find
        printf("please enter data you want to find in list\n> ");
        temp = get_input(buffer);
        pos = find(list,temp);
        if(pos >= 0){
          printf("element %s is in the list at index %d\n",temp,pos);
        }else{
          printf("element not found\n");
        }
        break;
      case 5: //delete
        printf("please enter index position that you want to delete in list\n> ");
        scanf("%d",&index);
        delete(list,index);
        displayList(list);
        break;
      default:
        usage();
        break;
    }
    //empty input stream when last input in stdio is string, 
    //if not and there is still char in stdin stream,
    //the fscan("%d") can not scan char to %d,
    //that will cause the program to terminate
    while((c=getchar()) !='\n' && c != EOF);
  }

  destory(list);
}

//create Node with data
Node* createNode(char* data){
  Node* n = (Node*) malloc(sizeof(Node));
  n->data = data;
  n->next = NULL;
  return n;
};

//create list
LinkedList* createList(){
  LinkedList* list = (LinkedList*) malloc(sizeof(LinkedList));
  list->top = NULL;
  list->current = NULL;
  list->length = 0;
  return list;
}

//return target node at index in list
Node* _go(LinkedList* list,int index){
  int pos = 0;
  Node* iter = list->top;
  while(iter != NULL && pos++ < index){
    iter = iter->next;
  }
  return iter;
}

//get data in index position
char* get(LinkedList* list,int index){
  Node *iter;

  if(isEmpty(list) || indexOutOfRange(list,index)){
    return NULL;
  }

  iter = _go(list,index);

  if(iter == NULL) return NULL;

  return iter->data;
}

//delete data in index position
int delete(LinkedList* list,int index){
  Node *iter, *delete;
   
  if(isEmpty(list) || indexOutOfRange(list,index)){
    return False;
  }
  //check is it delete the top node, if so, move top pointer to second Node
  //if there's no second node, top node will be NULL
  if(index == 0){
    delete = list->top;
    list->top = list->top->next;
    list->current = list->top;
  }else{
    iter = _go(list,index-1);
    delete = iter->next;
    iter->next = delete->next;
    //check is it delete the last node, if so, move current pointer to previous pointer
    //then delete the node
    if(list->length == (index +1)){
      list->current = iter;
    }
  }
  free(delete);
  list->length--;
  return True;
}

//free all node in linkedList
void destory(LinkedList* list){
  
  Node* iter;
  Node* delete;

  if(isEmpty(list)) return;
  iter = list->top;
  while(iter != NULL && iter->next != NULL){
    delete = iter;
    iter = iter->next;
    free(delete);
  }
  if(iter != NULL) free(iter);
  free(list);
  list == NULL;
}

//insert data in target index at list
int insert(LinkedList* list,int index,char* data){
  Node *iter,*new;

  if(list == NULL || index< 0 || index > list->length) return False;
  
  //if index is over the list by one, just add
  if(index == list->length) {
    add(list,data);
    return True;
  }

  new = createNode(data);
  
  //check the index is top node or not
  if(index == 0){
    new->next = list->top;
    list->top = new;
  }else{
    iter = _go(list,index-1);
    new->next = iter->next;
    iter->next = new;
  }
  list->length++;

  return True;
}

//find the data node in list, return index , if not found, return -1
int find(LinkedList* list,char* pattern){
  int pos = 0;
  Node *iter;

  if(isEmpty(list) || pattern == NULL) return -1;
  iter = list->top;
  do{
    if(!strcmp(iter->data,pattern)) return pos;
    iter = iter->next;
    pos++;
  }while(iter->next != NULL);
  if(!strcmp(iter->data,pattern)) return pos;
  return -1;
}

//append data to last of the list
int add(LinkedList* list,char* data){
  Node* node = createNode(data);

  if(list == NULL) return False;

  if(list->top == NULL){
    list->top = node;
  } else{
    list->current->next = node;
  }
  list->current = node;
  list->length++;
  return True;
}

int displayList(LinkedList* list){
  Node *iter;
  
  if(isEmpty(list)) {
    printf("[ ]\n"); 
    return False;
  }
  iter = list->top;

  printf("[");
  while(iter->next != NULL){
    printf("'%s',",iter->data);
    iter = iter->next;
  }
  printf("'%s']\n",iter->data);
  return True;
}

void usage(){
  printf("--usage--\n");
  printf("--(0):quit \n");
  printf("--(1):add \n");
  printf("--(2):get \n");
  printf("--(3):insert \n");
  printf("--(4):find \n");
  printf("--(5):delete \n");
}

//get the input and copy the string from buffer then return copyed string
char* get_input(char* buffer){
  char *input,c;
  input = (char*) calloc(strlen(buffer),sizeof(char));

  scanf("%80s",buffer);
  strncpy(input,buffer,strlen(buffer));

  return input;
};

//test functions, define TEST will call the testSuite before running 
void testSuite(){
  LinkedList *list = createList();
  //list created
  assert(list != NULL);
  //test add
  assert(add(list,"test2"));
  add(list,"test3");
  add(list,"test5");
  add(list,"test6");
  add(list,"test7");
  add(list,"test9");
  //test insert
  insert(list,3,"test4");
  //displayList(list);
  assert(!strncmp(get(list,3),"test4",5));
  //insert can insert into head and tail
  insert(list,0,"test1");
  assert(!strncmp(get(list,0),"test1",5));
  insert(list,list->length - 1,"test10");
  assert(!strncmp(get(list,list->length - 2),"test10",6));
  //test find
  assert(find(list,"test1")==0);
  //delete element
  assert(delete(list,2));
  delete(list,2);
  //test isEmpty
  assert(isEmpty(list)==False);
  delete(list,0);
  delete(list,0);
  delete(list,0);
  delete(list,0);
  delete(list,0);
  delete(list,0);
  delete(list,0);
  delete(list,0);
  assert(isEmpty(list)==True);
  //destory list
  destory(list);
  list = NULL;
}
