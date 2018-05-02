# armbrustlab.github.io

This repository holds [Jekyll](https://jekyllrb.com) site source for the [Armbrust Lab](https://armbrustlab.ocean.washington.edu) at the [University of Washington](https://www.washington.edu/). It uses the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) Jekyll theme.

## Local development installation
These instructions assume MacOS.

#### Ruby
First make sure Ruby and the Ruby Gems [Jekyll](https://jekyllrb.com) and [Bundler](https://bundler.io/) are installed. MacOS comes with a version of Ruby, or you can get it through [Homebrew](https://brew.sh/).

To install through Homebrew:

```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install ruby
gem install bundler jekyll
```

#### Clone the repository
```sh
git clone https://github.com/armbrustlab/armbrustlab.github.io.git
```

#### Start the local development webserver
```sh
cd armbrustlab.github.io
bundle install
bundle exec jekyll serve --livereload
```

This will start a local webserver on `http://localhost:4000` which will automatically reload the page when you make any changes to the site source. Sometimes the `--livereload` feature breaks and you'll need to manually stop the webserver with `ctrl-c` and then restart it.

## Source organization
Top-level pages are located in `_pages`. All other pages will be in a Jekyll collection folder in `collections`. e.g. pages under `/research/` will be at `collections/_research`. Images are located in `assets/images`.

All pages should be written in Markdown text format. [See here for a quick summary of major syntax](https://www.markdownguide.org/basic-syntax).

Links to places within the site should be created using the the [Liquid template](https://jekyllrb.com/docs/templates/) tag `{% link %}`. See [https://jekyllrb.com/docs/templates/#link](https://jekyllrb.com/docs/templates/#link). Look through existing site Markdown files to find examples of how to do this.

The easiest way to get started is to copy and edit an existing page Markdown file that has all the features you might want, e.g. lists, images, links.

## Common tasks
#### Adding a new lab member
To add a new lab member simply create a new Markdown file at `collections\_people` and name it `lastname.md`. It's easiest to copy an existing lab members profile file, then edit the [YAML Front Matter](https://jekyllrb.com/docs/frontmatter/) header at the top of the file and the actual Markdown content below. To add a profile picture add the image file to `/assets/images`, sized appropriately.

#### Creating a URL to another page on the site
Use the [`link` template tag](https://jekyllrb.com/docs/templates/#links) and basic markdown link creation syntax.

```
![seaflow]{% link _tools/seaflow.md %}
```

#### Adding an image
Note the use of the `link` tag to create the internal URL.

```
![Image alt text]({% link /assets/images/myimage.jpg %})
```

#### Aligning an image and text
See [https://mmistakes.github.io/minimal-mistakes/docs/utility-classes/](https://mmistakes.github.io/minimal-mistakes/docs/utility-classes/).

## Further reading
Refer to the [Jekyll](https://jekyllrb.com) and [theme](https://mmistakes.github.io/minimal-mistakes/) documentation or look around the site source to find more advanced usage.
