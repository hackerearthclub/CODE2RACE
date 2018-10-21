#include<iostream>
#include<stdlib.h>
#include<map>
#include<queue>
using namespace std;
struct bst{
	int data;
	struct bst *left;
	struct bst *right;
};
struct bst *root=NULL;
struct bst * create(struct bst *root,int data){
	struct bst *temp=(struct bst *)malloc(sizeof(struct bst ));
	temp->data=data;
	temp->left=NULL;
	temp->right=NULL;
	return temp;
}
struct bst * insert(struct bst *root,int data){
	if(root==NULL){
		struct bst *temp;
		temp=create(root,data);
		root=temp;
	
		return root;
	}
	else if(data<root->data){
		root->left=insert(root->left,data);
	}
	else{
		root->right=insert(root->right,data);
	}
	return root;
}
void diagonal(struct bst *root){ int dl;
	queue<pair<struct bst *,int> > q;
	map<int,vector<int> > m;
	q.push(make_pair(root,0));
	while(!q.empty()){
		pair<struct bst *,int> p=q.front();
		root=p.first;
		dl=p.second;
		q.pop();
		m[dl].push_back(root->data);
		if(root->left)
		q.push(make_pair(root->left,dl+1));
		if(root->right)
		q.push(make_pair(root->right,dl));
	}
	map<int,vector<int> >::iterator it;
	for(it=m.begin();it!=m.end();it++){
		vector<int>::iterator iter;
		for(iter=it->second.begin();iter!=it->second.end();iter++){
			cout<<*iter;
		}
		cout<<endl;
	}
}
int main(){
	root=insert(root,4);
	root=insert(root,6);
	root=insert(root,2);
	root=insert(root,3);
	root=insert(root,1);
	root=insert(root,5);
	diagonal(root);
}

