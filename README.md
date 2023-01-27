# Electronic-voting
Prototype implementation of a reliable and efficient electronic voting protocol which allows to obtain the election's results by performing the decrypting operation just once. For a voting system consisting of only two possibilities of votes which, for simplicity, we will consider $m=1$ (YES) and $m=0$ (NO), we design a protocol where a mother entity generates a public key and a private key and distributes one copy of the public key amognst those who can vote. The protocol is as follows:\
$1)$ $\underline{\text{Key generation}}$:\
Let $(N,p,q)$ be an RSA key, where $p$ and $q$ are prime numbers and $N=pq$. The public key is $pk=N$ and the secret key is $sk=d$, where $d$ is such that $d\equiv 1 \ mod \ N$ and $d\equiv 0 \ mod \ (p-1)(q-1)$.

$2)$ $\underline{\text{Encripting algorithm}}$:\
Let $N$ be Bob's public key. Then Alice can ecnrypt a message $m\in\mathbb{Z}_N$ as follows: randomly sampling $r\in\mathbb{Z}_N^*$ and computing $c=(1+N)^mr^N\ mod \ N^2$.

$3)$ $\underline{\text{Decrypting algorithm}}$:\
Bob, using his private key, $d$, and a ciphertext $c$ computes $m=\frac{c^d\ mod \ N^2-1}{N}$.

Let $Enc$ be the encrypting fuction, $Dec$ the decrypting function and let $c_1=Enc(m_1)$ and $c_2=Enc(m_2)$. By the construction of our protocol, $Dec(c_1·c_2)=m_1+m_2$. With this property, we can compute the election's results with just one decrypting operation. 

Let $c_1,...,c_n$ be all the votes, then the number of YES votes is $Dec(c_1\cdots c_n)$ and the number of NO votes is $n-Dec(c_1\cdots c_n)$.

