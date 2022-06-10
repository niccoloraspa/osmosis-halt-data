start:
	@docker build -t osmosis-halt:python .
	@docker run --name osmo-worker-0 -it -d -e START_HEIGHT=4707300 -e END_HEIGHT=4708800 -v $(PWD)/data:/app/data osmosis-halt:python
	@docker run --name osmo-worker-1 -it -d -e START_HEIGHT=4708801 -e END_HEIGHT=4710300 -v $(PWD)/data:/app/data osmosis-halt:python
	@docker run --name osmo-worker-2 -it -d -e START_HEIGHT=4710301 -e END_HEIGHT=4711800 -v $(PWD)/data:/app/data osmosis-halt:python 
	@docker run --name osmo-worker-3 -it -d -e START_HEIGHT=4711801 -e END_HEIGHT=4713064 -v $(PWD)/data:/app/data osmosis-halt:python

stop:
	@docker stop osmo-worker-{0,1,2,3}

clean:
	@docker rm -f osmo-worker-{0,1,2,3}