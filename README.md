# AWS Switch Role by Cookie
This script controle AWS Switch Role from Google Chrome cookies.


# Requirement

- Python 3
```
pycryptodome           3.10.1
keyring                23.0.1
```

- Google Chrome 

- mac OS 


# Installation

```shell
$ bash install.sh
# zsh shell 
$ source ~/.zshrc
# bash shell
$ source ~/.bashrc
```


# Example

## Switch role histpry list

```shell
$ sw ls
Set user : Default
Index  Account id         Role name                    View name                           Color   
------ ------------------ ---------------------------- ----------------------------------- --------
0      123456789012       switch-target-role           hoge                                E74C8E  
------ ------------------ ---------------------------- ----------------------------------- --------
1      123456789012       switch-target-role           fuga                                7838F9  
------ ------------------ ---------------------------- ----------------------------------- --------
```

## Switch role add

```shell
# ARN option
$ sw add arn:aws:iam::123456789012:role/switch-target-role
View name :hoge-fuga
Color [Enter(ramdom)]:D253F2

# No ARN option
$ sw add
Account id :123456789012
Role name :switch-target-role
View name :hoge-fuga
Color [Enter(ramdom)]:

```

## Switch role delete

```shell
$ sw del 0                                                
Index  Account id         Role name                    View name                           Color   
------ ------------------ ---------------------------- ----------------------------------- --------
0      123456789012       switch-target-role           hoge                                E74C8E  
Proceed [y/n]?y
```

## Chrome user change

```shell
$ sw profile        
New user number of Default [1~3 / Default]:1
```

## aws/config format output

```shell
$ sw output
[fuga]
role_arn = arn:aws:iam::123456789012:role/switch-target-role
color = 7838F9

[hoge-fuga]
role_arn = arn:aws:iam::123456789012:role/switch-target-role
color = D253F2

[hoge-fuga]
role_arn = arn:aws:iam::123456789012:role/switch-target-role
color = A72B1B

```


