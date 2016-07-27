package main


import (
    "fmt"
    "log"
    "net"
    "bufio"
)


func handleConnection(conn net.Conn) {

    data, err := bufio.NewReader(conn).ReadString('\n')

    if err != nil {
        log.Fatal("get client data error: ", err)
    }

    fmt.Printf("%#v\n", data)
    fmt.Fprintf(conn, "hello client\n")
    conn.Close()

}

func main() {

    ln, err := net.Listen("tcp", ":6019")
    if err != nil {
        panic(err)
    }

    for {
        conn, err := ln.Accept()
        if err != nil {
            log.Fatal("get client connection error: ", err)
        }
        go handleConnection(conn)
    }

}
