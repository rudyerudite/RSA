# RSA - Public Key Cryptosystem

RSA is an Public Key Cryptosystem  which is used to transmit messages over the internet, it is based on the principle of factoring large prime numbers. RSA is named after its inventors, Ronald L. Rivest, Adi Shamir, and Leonard M. Adleman, who created it at the Massachusetts Institute of Technology.This type of encryption is called Asymmetric cryptosystem, it is said so because the key for encryption and decryption are different.
They are the public key pair and the private key pair. As their name name suggests , public key pair is available to everyone, while the private key pair is for the individuals own use and is kept a secret. 


Now let us see the several steps used for encryption/decryption.

1. Key Generation
2. Key Distribution
3. Encryption/Decryption

Let us first define variables that will be repeatedly used:

1. <strong>p</strong>,<strong>q</strong> : Two very large primes 
2. <strong>n</strong> : Modulus, n = p*q
3. <strong>e</strong> : Public key exponent
4. <strong>d</strong> : Private key exponent
5. <strong>M</strong> : Unpadded message
3. <strong>m</strong> : Padded message
4. <strong>c</strong> : Ciphertext
5. $\varphi(n)$: [Euler's totient Function](https://en.wikipedia.org/wiki/Euler%27s_totient_function)


## Key Generation
1. Choose two distinct primes <strong>p</strong> and <strong>q</strong>. Both the primes must be chosen randomly and must be similar in magnitude. There should be a significant difference in the values of the primes otherwise it will become vulnerable to <strong>Fermat's Factorisation</strong> and we will see how and why is it so.
2. Compute $n = p*q$
3. Calculate the value of $\varphi(n) = (p-1)*(q-1)$ in this case. 
4. Choose an integer $e$ such that $1 < e < \varphi(n)$ and $gcd(e, \varphi(n)) = 1$. $e$ is often selected small and to be in the form of ${2^2}^i+1$ (where i is a positive integer) also known as [Fermat Numbers](https://en.wikipedia.org/wiki/Fermat_number), because it makes exponentiation more efficient. This makes it vulnerable to some attacks in some situations and we will see how we can prevent them.
5. Compute $d$ as $d = e^{-1} mod \varphi(n)$
6. The pair $(e, n)$ is known as public key and $(d, n)$ is known as private key.

## Key Distribution

Let us use an example to understand this,Suppose Alice wishes to send Bob a secret message, but the message will fall into the wrong hands if sent unsecured. Both Alice and Bob have a variety of padlocks, but they don't own the same ones, meaning that their keys cannot open the other's locks. In cryptographical terms, Bob must know Alice's public key to encrypt the message and Alice must use her private key to decrypt the message. To enable Bob to send his encrypted messages, Alice transmits her public key $(n, e)$ to Bob via a reliable, but not necessarily secret, route. Alice's private key $(d)$ is never distributed. Reliable channel --> The keys are sent without any alterations in their values.

## Encryption 
After Bob receives Alice's public key, he does the following operations:
1. Convert the message into integer form

2. Computes ciphertext $c = m^e \bmod{n}$

3. Now you have the ciphertext c ready to transmit using a reliable channel

## Decryption

After receiving the ciphertext c from Bob, Alice computes the following to get back the message:

1. Computes $m = c^d \bmod{n}$ . How this provides us the message we will see in the next section.

2. Convert the integer plaintext to the normal form.

### Proof of decryption using Euler's Theorem
Read about Euler's Theorem [here](https://en.wikipedia.org/wiki/Euler%27s_theorem). Now we have:

$c = M^e \bmod n$

$c^d \bmod n = M^{ed} \bmod n$

Since we have from Euler's theorem that: $a^{\varphi(n)} \equiv 1 \bmod{n}$,

We also know that, $ed \equiv 1 \bmod{\varphi (n)}$

We can convert this equation into: $ed = 1 + h{\varphi (n)}$

Using this we can now write

${\displaystyle m^{ed}=m^{1 + h\varphi (n)} = m(m^{\varphi (n)})^{h}\equiv m(1)^{h}\equiv m{\bmod {n}}}$
