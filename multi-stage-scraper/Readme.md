fst you need to enter into current project directory
        cd pathofprojectdirectory

 How to build the Docker image and please replace the image url without any processid(pid)

         docker buildx build --build-arg SCRAPE_URL=urlofimage -t my-scraping-app .

How to run the container.

        docker run -p 5003:5000 my-scraping-app

How to pass the URL to be scraped (via environment variables or
command-line arguments).

        we just provide the url in the build command itself

How to access the hosted scraped data.

        http://localhost:5003/image

