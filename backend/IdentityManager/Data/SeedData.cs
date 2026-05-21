using IdentityManager.Models;

namespace IdentityManager.Data;

public static class SeedData
{
    public static void Initialize(AppDbContext context)
    {
        if (context.Identities.Any()) return;

        // 1. Entitlements
        var entitlements = new List<Entitlement>
        {
            new Entitlement { Name = "Active Directory - Domain Users", Type = "AD Group", Description = "Basic network access" },
            new Entitlement { Name = "GitHub - Developer Access", Type = "Application", Description = "Access to source code repositories" },
            new Entitlement { Name = "AWS - ReadOnlyAccess", Type = "Cloud Role", Description = "Read-only access to AWS console" },
            new Entitlement { Name = "SAP - Finance User", Type = "Application", Description = "Access to finance modules" }
        };
        context.Entitlements.AddRange(entitlements);

        // 2. Connectors
        var adConnector = new Connector { Name = "Active Directory", Type = "Direct", Host = "ldap.example.com", ProvisioningConfig = "{\"samAccountName\": \"$username\", \"memberOf\": \"$groups\"}" };
        var sapConnector = new Connector { Name = "SAP ERP", Type = "Web Service", Host = "sap-api.example.com" };
        context.Connectors.AddRange(adConnector, sapConnector);

        // 3. Applications
        var hrmsApp = new Application { Name = "HRMS Central", Description = "Primary HR System", IsTrustedSource = true, ConnectorId = adConnector.Id };
        var financialApp = new Application { Name = "Finance Pro", Description = "Core financial system", ConnectorId = sapConnector.Id, Entitlements = new List<Entitlement> { entitlements[3] } };
        context.Applications.AddRange(hrmsApp, financialApp);

        // 4. Roles
        var devRole = new Role
        {
            Name = "Software Engineer",
            Description = "Standard access for developers",
            Entitlements = new List<Entitlement> { entitlements[0], entitlements[1], entitlements[2] }
        };
        var financeRole = new Role
        {
            Name = "Financial Analyst",
            Description = "Standard access for finance team",
            Entitlements = new List<Entitlement> { entitlements[0], entitlements[3] }
        };
        context.Roles.AddRange(devRole, financeRole);

        // 5. Identities
        var jdoe = new UserIdentity
        {
            Username = "jdoe",
            DisplayName = "John Doe",
            Email = "john.doe@example.com",
            Department = "Engineering",
            JobTitle = "Senior Dev",
            Roles = new List<Role> { devRole }
        };
        var asmith = new UserIdentity
        {
            Username = "asmith",
            DisplayName = "Alice Smith",
            Email = "alice.smith@example.com",
            Department = "Finance",
            JobTitle = "Analyst",
            Roles = new List<Role> { financeRole }
        };
        context.Identities.AddRange(jdoe, asmith);

        // 6. Access Requests with Workflows
        var request = new AccessRequest
        {
            RequesterId = asmith.Id,
            RequesterName = asmith.DisplayName,
            IdentityId = jdoe.Id,
            IdentityName = jdoe.DisplayName,
            RequestType = "Role",
            TargetId = financeRole.Id,
            TargetName = financeRole.Name,
            Status = "Pending",
            Comments = "Need access for cross-team project",
            WorkflowSteps = new List<WorkflowStep>
            {
                new WorkflowStep { Name = "Manager Approval", Approver = "Manager X", Status = "Approved", ActionedAt = DateTime.UtcNow.AddHours(-2) },
                new WorkflowStep { Name = "Security Review", Approver = "Security Team", Status = "Pending" }
            }
        };
        context.AccessRequests.Add(request);

        context.SaveChanges();
    }
}
