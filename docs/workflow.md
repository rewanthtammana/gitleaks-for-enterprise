## How Gitleaks for Enterprise work

1. Check the [gitleaks-for-enterprise](https://github.com/rewanthtammana/gitleaks-for-enterprise) repository. The directory structure is as follows - `allowlist/$USERNAME/$REPONAME/allowlist.toml`
    ![Show-Allowlist-Directory-Structure.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1653063995509/MXdgcvtBO.png)
2. Next step is to clone [gitleaks-for-enterprise](https://github.com/rewanthtammana/gitleaks-for-enterprise) & generate `gitleaks.toml`. We have a `base.toml` file with all the detection rules. The `allowlist` folder contains exceptions for all projects.
3. If this is your first time generating `gitleaks.toml`, this file would be equivalent to `base.toml` because there's no `allowlist.toml` for your target project yet.
    ```bash
    git clone https://github.com/rewanthtammana/gitleaks-for-enterprise
    cd gitleaks-for-enterprise
    python3 run.py allowlist/rewanthtammana/gitleaks-demo-repo/allowlist.toml > gitleaks.toml
     ```
    ![First-time-gitleaks-generation.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1653064164948/_PavTiKN-.png)
4. For this example, let's run it on a demo repository, [gitleaks-demo-repo](https://github.com/rewanthtammana/gitleaks-demo-repo). Clone this repo locally & run gitleaks on it. There are 6 leaks identified.
    ```bash
    git clone https://github.com/rewanthtammana/gitleaks-demo-repo /tmp/gitleaks-demo-repo
    gitleaks detect -c ./gitleaks.toml --source /tmp/gitleaks-demo-repo
    ```
    ![Gitleaks-First-Run.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1653064100802/1mqGKyZNF.png)
5. Append `-v` option to the above gitleaks command to view gitleaks information. I have leaked dummy values for demo purposes.
    ```bash
    gitleaks detect -c ./gitleaks.toml --source /tmp/gitleaks-demo-repo -v
    ```
    ![Gitleaks-first-output-analysis.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1653064192844/t2GqR1ugD.png)
6. Let's consider we revoked the above-identified Github key, `ghp_WtfdNeDljtnHfLaVePtZll6NQBqU6c0jiuSX`.
7. After a revocation, you can visit your `gitleaks-for-enterprise` setup & add this revocation as an exception.
    1. There are multiple ways to add exceptions based on commit id, value, file name, etc.
9. In this case, let's take the data as exception. Here it will be `ghp_WtfdNeDljtnHfLaVePtZll6NQBqU6c0jiuSX`
9. The allowlists should be in the below format for ease of organizing & access control, `allowlist/$USERNAME/$REPONAME/allowlist.toml`
10. In this case, we have to create a file `allowlist/rewanthtammana/gitleaks-demo-repo/allowlist.toml` with the following data as exception.

    ```toml
    # Rule specific white listing
    [[rules]]
        id = "8"
        [rules.allowlist]
            regexes = ['''ghp_WtfdNeDljtnHfLaVePtZll6NQBqU6c0jiuSX''']
    ```
11. Now generate a new `gitleaks.toml` file. This will be different from the base file because now we have an `allowlist.toml` file that will change the course.
    ```bash
    python3 run allowlist/rewanthtammana/gitleaks-demo-repo/allowlist.toml > gitleaks.toml
    ```
12. As we can see, the number of leaks reduce to 4 from 6. Also you can see that the github key we revoked, `ghp_WtfdNeDljtnHfLaVePtZll6NQBqU6c0jiuSX` isn't returned as a finding any further.
    ![Github-key-in-allowlist.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1653064255272/qYin5eVlD.png)
13. Similarly you can add more exceptions specific to your repo, in this case i.e `rewanthtammana/gitleaks-demo-repo`
