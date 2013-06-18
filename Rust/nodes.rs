#[link(name = "nodes", vers = "1.0")]

struct Node<T> {
	data: T
}

enum Link<T> {
	None,
	Some(~T)
}

struct LinkedNode<T> {
	data: T,
	mut right: Link<LinkedNode<T>>
}

struct BinaryNode<T> {
	data T,
	mut right: Link<BinaryNode<T>>,
	mut left: Link<BinaryNode<T>>
}
