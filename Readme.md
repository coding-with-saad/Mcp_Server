When we want to access something from a server, we must first connect to the internet using an IP address. Once connected, we use protocols like TCP or UDP to transfer data.

TCP (Transmission Control Protocol) is reliable and ensures complete, ordered data delivery. If any data is lost, it will be retransmitted. On the other hand, UDP (User Datagram Protocol) is faster and connectionless — it keeps sending data even if some of it is lost, making it suitable for live streaming and gaming.

From a programmer's perspective, this is simply called "data." Network engineers refer to it as "packets," and the actual content inside the packet is known as the "payload."

HTTP (HyperText Transfer Protocol) is responsible for structuring the entire communication. It includes the connection status, metadata (headers that specify routing, protocol, and app information), and the body, which contains the actual data being sent.