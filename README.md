create a new environment 

```sh
conda create -n name_env
```

activate a environment 

```sh
conda activate name_env
```

Remeber that `name_env` is equal to `blog`

update a environment from a file `yml`. 

```sh
conda env update -f environment.yml
```

For install a new package inside a enviroment

```sh
conda install name_package 
```

For save the requiremenyts of the environment in the yml file

```sh
conda env export > environment.yml
```

For download the changes from the repository to the actual branch `name_brach`

```git
git pull origin name_brach
```