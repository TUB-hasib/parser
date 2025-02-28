import argparse
import redis

def readRedis(url="localhost", port=6379):
    r = redis.Redis(host=url, port=port, db=0)
    print("Reading from Redis")



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Set a Redis key with expiration.")
    parser.add_argument("host", type=str, help="host name")
    parser.add_argument("port", type=int, help="port number")
    args = parser.parse_args()

    readRedis(args.host, args.port)

