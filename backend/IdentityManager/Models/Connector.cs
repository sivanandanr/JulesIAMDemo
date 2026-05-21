namespace IdentityManager.Models;

public class Connector
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty; // e.g. Active Directory, SAP, GitHub
    public string Type { get; set; } = string.Empty; // e.g. Direct, Web Service, Flat File
    public string Host { get; set; } = string.Empty;
    public string Status { get; set; } = "Healthy";
    public List<Application> Applications { get; set; } = new();
    public string ProvisioningConfig { get; set; } = "{}"; // JSON config for provisioning fields
}
