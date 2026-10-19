# Publishing SBOM Tools on GitHub

The working project contains a Markdown directory (`README.md`) and a fully static, interactive website (`docs/`). No build service or vendor account is required to run the site.

## 1. Create the repository

Create a **new public repository** on GitHub. Suggested name: `sbom-tools-directory` (the visible title remains **SBOM Tools**). Do not initialize it with a README or license, as those files are already in this project.

## 2. Push the project

Unzip the project, open a terminal in the extracted folder, and run:

```bash
git init
git add .
git commit -m "Launch SBOM Tools directory"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sbom-tools-directory.git
git push -u origin main
```

Replace `YOUR_USERNAME` with the GitHub account that owns the new repository.

## 3. Publish the website

In GitHub, open the repository and choose **Settings > Pages**. Under **Build and deployment**, select **Deploy from a branch**, then **main** and the **/docs** directory. Save. The site appears at `https://YOUR_USERNAME.github.io/sbom-tools-directory/` after GitHub Pages publishes it.

## 4. Maintain the listings

```bash
python3 scripts/validate.py
python3 scripts/build.py
```

Edit `data/tools.json` only, then commit the generated `README.md` and `docs/` files with the changed JSON. Pull requests are checked by `.github/workflows/validate.yml`.

## Publication status

The project files are published to `Drominaman/sbom-tools-directory`. GitHub Pages can be configured under **Settings > Pages**, selecting `main` and `/docs`.
